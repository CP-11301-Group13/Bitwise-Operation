<script>
import confetti from "https://cdn.skypack.dev/canvas-confetti";

import { ref, onMounted } from "vue";

const options = {
    ticks: 200,
    gravity: 0.75,
};

const func = ()=>{
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

}

func()
setInterval(() => {
    func()
}, 5000);
</script>

<template></template>

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
