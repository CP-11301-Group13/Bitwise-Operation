<script>
import _confetti from "https://cdn.skypack.dev/canvas-confetti";

const confetti = (args) => {
    // if (!targetIsVisible.value) return;

    _confetti(args);
};

import { ref, onMounted } from "vue";
import { useElementVisibility } from "@vueuse/core";

const target = ref(null);
const targetIsVisible = useElementVisibility(target);

const options = {
    ticks: 200,
    gravity: 0.75,
};

const func = () => {
    setTimeout(() => {
        confetti({
            particleCount: 100,
            origin: {
                x: -0.1,
            },
            angle: 55,
            ...options,
        });
    }, 500);
    confetti({
        particleCount: 150,
        origin: {
            x: 0.3,
            y: 0.9,
        },
        angle: 75,
        ...options,
    });

    setTimeout(() => {
        confetti({
            particleCount: 150,
            origin: {
                x: 0.7,
                y: 0.9,
            },
            angle: 105,
            ...options,
        });
    }, 1000);

    setTimeout(() => {
        confetti({
            particleCount: 100,
            origin: {
                x: 1.1,
            },
            angle: 125,
            ...options,
        });
    }, 1500);
};

let dispatched = false;
const dispatch = () => {
    if (!dispatched && targetIsVisible.value) {
        dispatched = true;

        func();
        setInterval(() => {
            func();
        }, 3500);
    } else if(!dispatched) {
        requestAnimationFrame(dispatch);
    }
};
dispatch();
requestAnimationFrame(dispatch);
</script>

<template>
    <div ref="target" style="position: fixed"></div>
</template>

<style>
button {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    color: #4fc08d;
    background: none;
    border: solid 1px;
    border-radius: 2em;
    padding: 0.75em 2em;
}
</style>
