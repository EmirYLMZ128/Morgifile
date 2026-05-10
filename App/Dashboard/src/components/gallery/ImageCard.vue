<template>
  <div class="image-card" @click="$emit('selectImage', img)">
    <div v-if="!isLoaded && !isBroken" class="placeholder-square">
    </div>
    
    <div v-if="isBroken" class="placeholder-square">
      <i class="fas fa-image" style="opacity: 0.3;"></i>
      <i class="fas fa-slash" style="position: absolute; font-size: 2.5rem; opacity: 0.5;"></i>
    </div>

    <img 
      v-show="!isBroken"
      :style="{ opacity: isLoaded ? 1 : 0, position: isLoaded ? 'relative' : 'absolute', top: 0, left: 0, width: '100%', height: '100%', objectFit: 'cover' }"
      :src="imgSrc" 
      loading="lazy"
      alt="" 
      @load="onImageLoad" 
      @error="handleImageError" 
    />
    
    <div class="card-overlay"></div>
    <div class="card-actions" @click.stop>
      <template v-if="img.isDeleted">
        <button class="card-btn custom-btn custom-fire" @click="$emit('permanentDelete', img.id)" title="Delete permanently">
          <img class="custom-icon default-icon" src="../../assets/ActionIcons/firePas.svg" alt="Permanent Delete" />
          <img class="custom-icon active-icon" src="../../assets/ActionIcons/fireAct.svg" alt="Permanent Delete Active" />
        </button>
        <button class="card-btn custom-btn custom-cat" @click="$emit('restoreImage', img.id)" title="Restore">
          <img class="custom-icon default-icon" src="../../assets/ActionIcons/changeCatPas.svg" alt="Restore" />
          <img class="custom-icon active-icon" src="../../assets/ActionIcons/changeCatAct.svg" alt="Restore Active" />
        </button>
      </template>
      
      <template v-else-if="img.isDead">
        <button class="card-btn custom-btn custom-trash" @click="$emit('moveToTrash', img.id)" title="Move to trash">
          <img class="custom-icon default-icon" src="../../assets/ActionIcons/trashPas.svg" alt="Trash" />
          <img class="custom-icon active-icon" src="../../assets/ActionIcons/trashAct.svg" alt="Trash Active" />
        </button>
      </template>
      
      <template v-else>
        <button class="card-btn custom-btn custom-fav" :class="{ 'active-fav': img.isFavorite }" @click="$emit('toggleFavorite', img.id)" title="Favorite">
          <img class="custom-icon default-icon" src="../../assets/ActionIcons/favPas.svg" alt="Favorite" />
          <img class="custom-icon active-icon" src="../../assets/ActionIcons/favAct.svg" alt="Favorite Active" />
        </button>
        
        <button v-if="!img.isFavorite" class="card-btn custom-btn custom-trash" @click="$emit('moveToTrash', img.id)" title="Move to trash">
          <img class="custom-icon default-icon" src="../../assets/ActionIcons/trashPas.svg" alt="Trash" />
          <img class="custom-icon active-icon" src="../../assets/ActionIcons/trashAct.svg" alt="Trash Active" />
        </button>
        
        <button class="card-btn custom-btn custom-cat" @click="$emit('changeCategory', img.id)" title="Change category">
          <img class="custom-icon default-icon" src="../../assets/ActionIcons/changeCatPas.svg" alt="Category" />
          <img class="custom-icon active-icon" src="../../assets/ActionIcons/changeCatAct.svg" alt="Category Active" />
        </button>
      </template>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, computed, onMounted } from 'vue';

const props = defineProps({
  img: { type: Object, required: true }
});

const emit = defineEmits(['selectImage', 'permanentDelete', 'restoreImage', 'moveToTrash', 'toggleFavorite', 'changeCategory', 'markDead']);

const isLoaded = ref(false);
const isBroken = ref(false);

const imgSrc = computed(() => {
  if (props.img.isDead) return `http://127.0.0.1:8000/thumbnail/${props.img.id}`;
  if (props.img.isSafe && props.img.SafePath) return `http://127.0.0.1:8000/safe-file?path=${encodeURIComponent(props.img.SafePath)}`;
  if (props.img.isCORS || props.img.proxyTried) return `http://127.0.0.1:8000/proxy/image?url=${encodeURIComponent(props.img.originalUrl)}`;
  return props.img.originalUrl;
});

watch(imgSrc, (newSrc, oldSrc) => {
  if (newSrc !== oldSrc) {
    isLoaded.value = false;
    isBroken.value = false;
  }
});

function onImageLoad() {
    isLoaded.value = true;
}

function handleImageError(e) {
  if (props.img.isDead) {
    isBroken.value = true;
    return;
  }
  
  if (props.img.proxyTried || imgSrc.value.includes('/proxy/image')) {
    emit('markDead', props.img.id);
  } else {
    props.img.proxyTried = true; // This will trigger the computed imgSrc and watcher automatically
  }
}
</script>

<style scoped>
.custom-btn {
  display: flex;
  align-items: center;
  justify-content: center;
}
.custom-btn .active-icon {
  display: none;
}
.custom-btn:hover .default-icon,
.custom-fav.active-fav .default-icon {
  display: none;
}
.custom-btn:hover .active-icon,
.custom-fav.active-fav .active-icon {
  display: block;
}

.custom-fav .active-icon { filter: drop-shadow(0 0 6px rgba(251, 191, 36, 0.7)); }
.custom-trash .active-icon { filter: drop-shadow(0 0 6px rgba(239, 68, 68, 0.7)); }
.custom-cat .active-icon { filter: drop-shadow(0 0 6px rgba(99, 102, 241, 0.7)); }
.custom-fire .active-icon { filter: drop-shadow(0 0 6px rgba(239, 68, 68, 0.8)); }

.custom-icon {
  width: 1.6rem;
  height: 1.6rem;
  object-fit: contain;
}
</style>
