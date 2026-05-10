<template>
  <div v-if="isVisible" class="detail-modal-overlay" style="display: flex" @click="$emit('close')">
    <div class="detail-modal-container" @click.stop>
      <div class="detail-left">
        <img :src="imgSrc" loading="lazy" alt="Image Detail">
      </div>

      <div class="detail-right">
        <div class="detail-info-group">
          <h3>Image Details</h3>
          
          <div class="info-item">
            <span class="info-label">Site:</span>
            <span class="info-value">{{ img.site || 'N/A' }}</span>
          </div>
          
          <div class="info-item" v-if="img.sourceUrl">
            <span class="info-label">Source Post:</span>
            <a :href="img.sourceUrl" target="_blank" class="info-value" style="color: var(--accent); text-decoration: none;">Go to Original Post 🔗</a>
          </div>
          
          <div class="info-item">
            <span class="info-label">URL:</span>
            <a :href="img.originalUrl" target="_blank" class="info-link">Go to Source <i class="fas fa-external-link-alt"></i></a>
          </div>
          
          <div class="info-item">
            <span class="info-label">Category:</span>
            <span class="info-value">{{ img.category }}</span>
          </div>

          <div class="info-item">
            <span class="info-label">Main Color:</span>
            <div style="display: flex; align-items: center; gap: 8px;">
              <div @click="copyColor(img.mainColor)" class="color-circle" :style="{ backgroundColor: img.mainColor || 'transparent' }" :title="img.mainColor ? 'Copy ' + img.mainColor : ''"></div>
              <span class="info-value" style="font-family: monospace;">{{ img.mainColor || '---' }}</span>
              <span v-if="copiedColor === img.mainColor" :key="'main-' + copyKey" class="copied-pill">Copied!</span>
            </div>
          </div>

          <div class="info-item">
            <span class="info-label">Size:</span>
            <span class="info-value" id="info-size">{{ img.width || 0 }}px x {{ img.height || 0 }}px</span>
          </div>

          <hr class="detail-divider">

          <template v-if="!img.isDead">
            <div class="ai-section">
              <div class="info-label">Color Palette:</div>
              <div class="ai-content">
                <div v-if="parsedColors" style="display: flex; gap: 10px; margin-top: 5px; align-items: center;">
                  <div v-for="c in parsedColors" :key="c" @click="copyColor(c)" class="color-circle" :style="{ backgroundColor: c }" :title="'Copy ' + c"></div>
                  <span v-if="copiedColor && parsedColors.includes(copiedColor)" :key="'pal-' + copyKey" class="copied-pill">Copied!</span>
                </div>
                <button v-else class="outline-btn" @click="extractColors" :class="{ disabled: isExtracting }" title="Extract 5 dominant colors">
                  <i :class="isExtracting ? 'fas fa-spinner fa-spin' : 'fas fa-palette'"></i> 
                  {{ isExtracting ? 'Extracting...' : 'Extract Color' }}
                </button>
              </div>
            </div>
            
            <div class="ai-section">
              <div class="info-label">Search Engines:</div>
              <div class="ai-content">
                <button class="outline-btn" @click="openLink(`https://lens.google.com/uploadbyurl?url=${safeUrl}`)" title="Search on Google Lens">
                  <i class="fas fa-search"></i> Lens
                </button>
                <button class="outline-btn" @click="openLink(`https://yandex.com/images/search?rpt=imageview&url=${safeUrl}`)" title="Find similar on Yandex">
                  <i class="fab fa-yandex-international"></i> Yandex
                </button>
                <button class="outline-btn" @click="openLink(`https://tineye.com/search?url=${safeUrl}`)" title="Find source with TinEye">
                  <i class="fas fa-eye"></i> TinEye
                </button>
              </div>
            </div>
          </template>
        </div>

        <div class="action-btn-list">
          <button class="action-btn nav-arrow" :disabled="!hasPrev" :class="{ disabled: !hasPrev }" @click="hasPrev && $emit('navigate', -1)">
            <i class="fas fa-arrow-left"></i>
          </button>

          <template v-if="img.isDead">
            <button class="action-btn custom-action-btn custom-trash" @click="$emit('moveToTrash', img.id)" title="Move to Trash">
              <img class="custom-icon default-icon" src="../../assets/ActionIcons/trashPas.svg" alt="Trash" />
              <img class="custom-icon active-icon" src="../../assets/ActionIcons/trashAct.svg" alt="Trash Active" />
            </button>
          </template>
          <template v-else>
            <button class="action-btn custom-action-btn custom-fav" :class="{ 'active-fav': img.isFavorite }" @click="$emit('toggleFavorite', img.id)" title="Favorite">
              <img class="custom-icon default-icon" src="../../assets/ActionIcons/favPas.svg" alt="Favorite" />
              <img class="custom-icon active-icon" src="../../assets/ActionIcons/favAct.svg" alt="Favorite Active" />
            </button>
            <button class="action-btn custom-action-btn custom-save" :class="{ 'active-safe': img.isSafe }" :disabled="img.isSafe" :style="{ cursor: img.isSafe ? 'default' : 'pointer' }" @click="!img.isSafe && $emit('handleSafeArchive', img.id)" title="Safe Archive">
              <img class="custom-icon default-icon" src="../../assets/ActionIcons/savePas.svg" alt="Save Archive" />
              <img class="custom-icon active-icon" src="../../assets/ActionIcons/saveAct.svg" alt="Save Archive Active" />
            </button>
            <button class="action-btn custom-action-btn custom-cat" @click="$emit('changeCategory', img.id)" title="Change Category">
              <img class="custom-icon default-icon" src="../../assets/ActionIcons/changeCatPas.svg" alt="Category" />
              <img class="custom-icon active-icon" src="../../assets/ActionIcons/changeCatAct.svg" alt="Category Active" />
            </button>
            <button v-if="!img.isFavorite" class="action-btn custom-action-btn custom-trash" @click="$emit('moveToTrash', img.id)" title="Move to Trash">
              <img class="custom-icon default-icon" src="../../assets/ActionIcons/trashPas.svg" alt="Trash" />
              <img class="custom-icon active-icon" src="../../assets/ActionIcons/trashAct.svg" alt="Trash Active" />
            </button>
          </template>

          <button class="action-btn nav-arrow" :disabled="!hasNext" :class="{ disabled: !hasNext }" @click="hasNext && $emit('navigate', 1)">
            <i class="fas fa-arrow-right"></i>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { filteredImages } from '@/store';

const props = defineProps({
  isVisible: { type: Boolean, required: true },
  img: { type: Object, default: () => ({}) }
});

const emit = defineEmits(['close', 'showComingSoon', 'moveToTrash', 'toggleFavorite', 'handleSafeArchive', 'changeCategory', 'navigate']);

const isExtracting = ref(false);
const copiedColor = ref(null);
const copyKey = ref(0);
let copiedTimeout = null;

const parsedColors = computed(() => {
    if (!props.img || !props.img.colors) return null;
    try {
        return typeof props.img.colors === 'string' ? JSON.parse(props.img.colors) : props.img.colors;
    } catch(e) { return null; }
});

async function extractColors() {
    if (isExtracting.value || !props.img.id) return;
    isExtracting.value = true;
    try {
        const res = await fetch(`http://127.0.0.1:8000/images/${props.img.id}/extract-colors`, { method: "POST" });
        if (res.ok) {
            const data = await res.json();
            props.img.colors = data.colors;
        } else {
            console.error('Color extraction failed.');
        }
    } catch (e) {
        console.error(e);
    } finally {
        isExtracting.value = false;
    }
}

async function copyColor(hex) {
    if(!hex) return;
    try {
        await navigator.clipboard.writeText(hex);
        copiedColor.value = hex;
        copyKey.value++; // Force Vue to re-create the element and replay CSS animation
        
        if(copiedTimeout) clearTimeout(copiedTimeout);
        copiedTimeout = setTimeout(() => {
            if(copiedColor.value === hex) copiedColor.value = null;
        }, 2000);
    } catch(e) {
        console.error('Copy failed', e);
    }
}

const currentIndex = computed(() => {
    return filteredImages.value.findIndex(i => i.id === props.img.id);
});

const hasPrev = computed(() => currentIndex.value > 0);
const hasNext = computed(() => currentIndex.value >= 0 && currentIndex.value < filteredImages.value.length - 1);

function handleKeydown(e) {
    if (!props.isVisible) return;
    if (e.key === 'ArrowLeft' && hasPrev.value) {
        emit('navigate', -1);
    } else if (e.key === 'ArrowRight' && hasNext.value) {
        emit('navigate', 1);
    }
}

onMounted(() => {
    window.addEventListener('keydown', handleKeydown);
});

onUnmounted(() => {
    window.removeEventListener('keydown', handleKeydown);
});

const safeUrl = computed(() => encodeURIComponent(props.img.originalUrl || ''));

const imgSrc = computed(() => {
  if (!props.img || !props.img.id) return '';
  if (props.img.isDead) return `http://127.0.0.1:8000/thumbnail/${props.img.id}`;
  if (props.img.isSafe && props.img.SafePath) return `http://127.0.0.1:8000/safe-file?path=${encodeURIComponent(props.img.SafePath)}`;
  if (props.img.isCORS || props.img.proxyTried) return `http://127.0.0.1:8000/proxy/image?url=${encodeURIComponent(props.img.originalUrl)}`;
  return props.img.originalUrl;
});

function openLink(url) {
  window.open(url, '_blank');
}
</script>

<style scoped>
.custom-action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 12px;
}
.custom-action-btn:hover {
  background: rgba(255, 255, 255, 0.03) !important;
  border-color: var(--border) !important;
}
.custom-action-btn .active-icon {
  display: none;
}
.custom-action-btn:hover .default-icon,
.custom-fav.active-fav .default-icon {
  display: none;
}
.custom-action-btn:hover .active-icon,
.custom-fav.active-fav .active-icon {
  display: block;
}

.custom-fav .active-icon { filter: drop-shadow(0 0 6px rgba(251, 191, 36, 0.7)); }
.custom-trash .active-icon { filter: drop-shadow(0 0 6px rgba(239, 68, 68, 0.7)); }
.custom-cat .active-icon { filter: drop-shadow(0 0 6px rgba(99, 102, 241, 0.7)); }
.custom-save .active-icon { filter: drop-shadow(0 0 6px rgba(16, 185, 129, 0.7)); }

.custom-icon {
  width: 1.5rem;
  height: 1.5rem;
  object-fit: contain;
}
</style>
