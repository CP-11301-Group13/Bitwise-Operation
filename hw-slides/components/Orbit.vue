<script setup lang="ts">
import { ref, onMounted } from 'vue'

const rad = 50;
const v = 0.05;

const rx = ref(Math.random())
const ry = ref(Math.random())
const rz = ref(Math.random())

const x = ref(0)
const y = ref(0)
const z = ref(0)

const scale = ref(1)

onMounted(() => {
    const updatePosition = () => {
        rx.value += Math.random() * v;
        ry.value += Math.random() * v;
        rz.value += Math.random() * v;
        x.value = rad * Math.cos(rx.value)
        y.value = rad * Math.sin(ry.value)
        z.value = rad * Math.sin(rz.value)
        scale.value = 1 / (1 + z.value / rad)
        requestAnimationFrame(updatePosition)
    }
    updatePosition()
})
</script>

<template>
    <div :style="{
        transform: `translate3d(${x}px, ${y}px, ${z}px)`,
        scale: scale,
     }">
        <slot /> <!-- Render the passed child component -->
    </div>
</template>