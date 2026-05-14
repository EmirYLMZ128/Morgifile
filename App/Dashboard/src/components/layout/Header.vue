<template>
  <header class="top-header">
    <div class="header-left">
      <div class="current-category-info" id="active-category-display">
        <span id="active-category-name">{{ store.activeCategory }}</span>
      </div>
    </div>
    <div class="header-right">
      <button v-if="!['Trash', 'Graveyard'].includes(store.activeCategory)"
              class="action-btn edit relative"
              :style="autoScrollSpeed > 0 ? 'background: var(--accent); color: white; box-shadow: 0 0 20px rgba(99, 102, 241, 0.5); border-color: transparent; transform: translateY(-2px);' : ''"
              @click="toggleAutoScroll"
              :title="scrollTitle">
        <i class="fas" :class="autoScrollSpeed === 3 ? 'fa-stop' : 'fa-angle-double-down'"></i>
        <span v-if="autoScrollSpeed > 0" class="absolute -bottom-1 -right-1 text-[10px] bg-[#EF4444] text-white rounded-full w-4 h-4 flex items-center justify-center font-bold shadow-sm">
          {{ autoScrollSpeed }}
        </span>
      </button>

      <div v-if="store.activeCategory === 'Color Match'" class="flex items-center justify-center relative ml-2" title="Pick Color">
        <input type="color" v-model="store.colorMatchHex" class="w-8 h-8 rounded cursor-pointer border-none bg-transparent outline-none p-0" />
      </div>

      <button v-if="store.activeCategory === 'Trash'" 
              class="pill-btn custom-pill-btn" 
              @click="$emit('emptyTrash')">
        <img class="custom-icon default-icon" src="../../assets/ActionIcons/firePas.svg" alt="Empty Trash" />
        <img class="custom-icon active-icon" src="../../assets/ActionIcons/fireAct.svg" alt="Empty Trash Active" />
        Empty Trash
      </button>
      
      <button class="action-btn ml-2" @click="store.isDarkMode = !store.isDarkMode" :title="store.isDarkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode'">
        <i class="fas" :class="store.isDarkMode ? 'fa-sun' : 'fa-moon'"></i>
      </button>

      <div v-if="isCustomCategory" class="flex gap-2">
        <button class="action-btn edit" @click="$emit('renameCategory')" title="Rename Category">
          <i class="fas fa-edit"></i>
        </button>
        <button class="action-btn delete" @click="$emit('deleteCategory')" title="Delete Category">
          <i class="fas fa-trash"></i>
        </button>
      </div>
    </div>
  </header>
</template>

<script setup>
import { computed, ref, watch, onUnmounted } from 'vue';
import { store } from '@/store';

const isCustomCategory = computed(() => {
  const builtIns = ["All Images", "Favorites", "Graveyard", "Trash", "Color Match"];
  return !builtIns.includes(store.activeCategory);
});

const autoScrollSpeed = ref(0);
let scrollInterval = null;

const scrollTitle = computed(() => {
  if (autoScrollSpeed.value === 0) return 'Start Auto Scroll (Slow)';
  if (autoScrollSpeed.value === 1) return 'Speed: Normal';
  if (autoScrollSpeed.value === 2) return 'Speed: Fast';
  return 'Stop Auto Scroll';
});

const toggleAutoScroll = () => {
  autoScrollSpeed.value = (autoScrollSpeed.value + 1) % 4; // 0, 1, 2, 3
  
  if (scrollInterval) {
    clearInterval(scrollInterval);
    scrollInterval = null;
  }

  if (autoScrollSpeed.value > 0) {
    const speeds = { 1: 2, 2: 6, 3: 15 }; // Scroll steps in pixels
    const step = speeds[autoScrollSpeed.value];
    
    scrollInterval = setInterval(() => {
      const container = document.querySelector('.gallery-container');
      if (container) {
        container.scrollTop += step;
      }
    }, 20);
  }
};

watch(() => store.activeCategory, () => {
  if (autoScrollSpeed.value > 0) {
    autoScrollSpeed.value = 0;
    if (scrollInterval) {
      clearInterval(scrollInterval);
      scrollInterval = null;
    }
  }
});

onUnmounted(() => {
  if (scrollInterval) clearInterval(scrollInterval);
});
</script>

<style scoped>
.custom-pill-btn {
  background: rgba(255, 255, 255, 0.03);
  color: var(--text-dim);
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.3s ease;
}
.custom-pill-btn .active-icon {
  display: none;
}
.custom-pill-btn:hover {
  border-color: rgba(239, 68, 68, 0.4);
  background: rgba(239, 68, 68, 0.08);
  color: #EF4444;
  box-shadow: 0 0 15px rgba(239, 68, 68, 0.15);
}
.custom-pill-btn:hover .default-icon {
  display: none;
}
.custom-pill-btn:hover .active-icon {
  display: block;
  filter: drop-shadow(0 0 6px rgba(239, 68, 68, 0.7));
}
.custom-icon {
  width: 1.4rem;
  height: 1.4rem;
  object-fit: contain;
}
</style>
