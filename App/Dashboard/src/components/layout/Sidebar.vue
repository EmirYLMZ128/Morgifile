<template>
  <aside class="sidebar h-full" :class="{ 'collapsed': isCollapsed }">
    <div class="sidebar-header">
      <div class="logo">
        <img :src="currentLogo" 
             :alt="isCollapsed ? 'Morgi Icon' : 'Morgi Logo'" 
             class="logo-img">
      </div>
      <button class="toggle-btn" @click="isCollapsed = !isCollapsed">
        <i class="fas" :class="isCollapsed ? 'fa-chevron-right' : 'fa-chevron-left'"></i>
      </button>
    </div>
    
    <nav class="nav-menu">
      <div class="nav-section"><span class="section-text">General</span></div>
      <div class="nav-item" :class="{ active: store.activeCategory === 'All Images' }" @click="setCategory('All Images')" :title="isCollapsed ? 'All Images' : ''">
        <i class="fas fa-th-large"></i> <span class="nav-text">All Images</span>
      </div>
      <div class="nav-item" :class="{ active: store.activeCategory === 'Favorites' }" @click="setCategory('Favorites')" :title="isCollapsed ? 'Favorites' : ''">
        <i class="fas fa-star"></i> <span class="nav-text">Favorites</span>
      </div>
      <div class="nav-item" :class="{ active: store.activeCategory === 'Graveyard' }" @click="setCategory('Graveyard')" :title="isCollapsed ? 'Graveyard' : ''">
        <i class="fas fa-skull-crossbones"></i> <span class="nav-text cat-name">Graveyard</span>
      </div>
      <div class="nav-item" :class="{ active: store.activeCategory === 'Color Match' }" @click="setCategory('Color Match')" :title="isCollapsed ? 'Color Match' : ''">
        <i class="fas fa-palette"></i> <span class="nav-text">Color Match</span>
      </div>
      <div class="nav-item" :class="{ active: store.activeCategory === 'Trash' }" @click="setCategory('Trash')" :title="isCollapsed ? 'Trash' : ''">
        <i class="fas fa-trash-alt"></i> <span class="nav-text">Trash</span>
      </div>
      
      <div class="nav-section"><span class="section-text">Categories</span></div>
      <div id="sidebar-categories" class="flex-col pb-4">
        <div v-for="cat in visibleCategories" :key="cat" 
             class="nav-item category-item" 
             :class="{ active: store.activeCategory === cat }" 
             @click="setCategory(cat)"
             :title="isCollapsed ? cat : ''">
          <span class="cat-icon-text">{{ cat.substring(0, 2).toUpperCase() }}</span>
          <span class="nav-text cat-name">{{ cat }}</span>
        </div>
      </div>
    </nav>

    <button class="btn-manage mt-auto" @click="$emit('openManageCategories')" :title="isCollapsed ? 'Manage Categories' : ''">
      <i class="fas fa-sliders-h"></i> <span class="nav-text">Manage Categories</span>
    </button>
  </aside>
</template>

<script setup>
import { ref, computed } from 'vue';
import { store } from '@/store';

// Logos
import logoFull from '@/assets/MainIcons/mainLogoText.svg';
import logoFullDark from '@/assets/MainIcons/mainLogoText4Dark.svg';
import logoIcon from '@/assets/MainIcons/mainLogo.svg';
import logoIconDark from '@/assets/MainIcons/mainLogo4Dark.svg';

const emit = defineEmits(['openManageCategories']);
const isCollapsed = ref(false);

const visibleCategories = computed(() => {
  return store.categories.filter(cat => {
    if (cat === 'Uncategorized Favorites') {
      return store.images.some(img => img.category === cat && !img.isDeleted && !img.isDead);
    }
    return true;
  });
});

const currentLogo = computed(() => {
  if (store.isDarkMode) {
    return isCollapsed.value ? logoIconDark : logoFullDark;
  } else {
    return isCollapsed.value ? logoIcon : logoFull;
  }
});

function setCategory(cat) {
  store.activeCategory = cat;
}
</script>

<style scoped>
.logo-img {
  height: 44px;
  width: auto;
  transition: all 0.3s ease;
  filter: drop-shadow(0 0 10px rgba(37, 99, 235, 0.25));
}

.sidebar.collapsed .logo-img {
  height: 40px;
}
</style>
