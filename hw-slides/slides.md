---
theme: dracula
# some information about your slides (markdown enabled)
title: Group 20
# info: |
#     ## Slidev Starter Template
#     Presentation slides for developers.

#     Learn more at [Sli.dev](https://sli.dev)
# class: text-center
drawings:
    persist: false
transition: slide-left
mdc: true
---

<style>
  @keyframes marquee {
    from {
      transform: translateX(calc(-33% - 14px));
    }
    to {
      transform: translateX(0);
    }
  }

  :root{
    /* --duration: 10000000s; */
    --duration: 12s;

  }
</style>

# Bitwise Operations

### Group 20

<div class="fixed left-0 bottom-0 w-[100%] h-[100vh] overflow-hidden h-fit-content">
<div style='animation: marquee var(--duration) linear infinite;' class='absolute bottom-5 [&>*]:flex-1 [&>*]:text-nowrap	 left-0  flex mr-5 gap-5 items-center'>
  <kbd style="font-size: 1rem; line-height:1.35rem; color: var(--green)">B10401006 洪愷希</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem; color: var(--comment)">B12505047 陳澤諒</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem; color: var(--orange)">B11801005 何宗蕘</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem; color: var(--pink)">R13944053 温文安</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem; color: var(--red)">B12902090 張玉慧</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem; color: var(--green)">B10401006 洪愷希</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem; color: var(--comment)">B12505047 陳澤諒</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem; color: var(--orange)">B11801005 何宗蕘</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem; color: var(--pink)">R13944053 温文安</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem; color: var(--red)">B12902090 張玉慧</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem; color: var(--green)">B10401006 洪愷希</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem; color: var(--comment)">B12505047 陳澤諒</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem; color: var(--orange)">B11801005 何宗蕘</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem; color: var(--pink)">R13944053 温文安</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem; color: var(--red)">B12902090 張玉慧</kbd>
</div>
</div>

---

# Problem

給定一個 **32-bit 無號整數**，請將它在二進位表示下的**奇數位**和**偶數位**反轉後輸出。

### Example

<style>
  thead {
    opacity: 0.75;
    font-size: 1rem;
  }
  tbody {
    td:nth-child(3) ,
    td:nth-child(5) ,
    td:nth-child(7) ,
    td:nth-child(9) ,
    td:nth-child(11) ,
    td:nth-child(13) ,
    {
      color: var(--red);
    }

    td:nth-child(2) ,
    td:nth-child(4) ,
    td:nth-child(6) ,
    td:nth-child(8) ,
    td:nth-child(10) ,
    td:nth-child(12) ,
    td:nth-child(14) ,
    {
      color: var(--cyan);
    }
  
  }
</style>

| 輸入 | 32  | 16  | 8   | 4   | 2   | 1   |      | 32  | 16  | 8   | 4   | 2   | 1   | 輸出 |
| ---- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | ---- |
| 23   | 0   | 1   | 0   | 1   | 1   | 1   | ➡ ️ | 1   | 0   | 1   | 0   | 1   | 1   | 43   |
| 13   | 0   | 0   | 1   | 1   | 0   | 1   | ➡   | 0   | 0   | 1   | 1   | 1   | 0   | 14   |
| 63   | 1   | 1   | 1   | 1   | 1   | 0   | ➡   | 1   | 1   | 1   | 1   | 0   | 1   | 62   |

---

layout: two-cols
layoutClass: gap-16
transition: none

---

# Solution (1)

Pseudocode 😃

````md magic-move {lines: true}
```py {*|4,5|7,8|9|11,12|*}
x = int(input())

res = 0
mask1 = 0
mask2 = 1
for i in range(?):
  bit1 = x & mask1
  bit2 = x & mask2
  res |= (bit1 << ?) | (bit2 >> ?)

  mask1 = mask1 << ??
  mask2 = mask2 << ??
```
````

::right::

## Example: 23

<div>
</div>

<style>
  div.container {
    display: flex;
    gap: 50px;
    font-size: 1.5rem;
    /* span {
      width: 32px;
    } */
    span:nth-child(even){
      color: var(--comment);
    }
    span:nth-child(odd){
      color: var(--red);
    }
  }
</style>

<div
  class="container mt-32px"
>
  <span v-motion :initial="{ x: 0 }" :enter="{ opacity: 1}" :click-11="{ x: 64 } " :leave="{ opacity: 0.5}" >0</span>
  <span v-motion :initial="{ x: 0 }" :enter="{ opacity: 1}" :click-11="{ x: -64 }" :leave="{ opacity: 0.5}" >1</span>
  <span v-motion :initial="{ x: 0 }" :enter="{ opacity: 1}" :click-9="{ x: 64 }  " :leave="{ opacity: 0.5}" >0</span>
  <span v-motion :initial="{ x: 0 }" :enter="{ opacity: 1}" :click-9="{ x: -64 } " :leave="{ opacity: 0.5}" >1</span>
  <span v-motion :initial="{ x: 0 }" :enter="{ opacity: 1}" :click-7="{ x: 64 }  " :leave="{ opacity: 0.5}" >1</span>
  <span v-motion :initial="{ x: 0 }" :enter="{ opacity: 1}" :click-7="{ x: -64 } " :leave="{ opacity: 0.5}" >1</span>
</div>

<div
  class="container bg-[var(--comment)] w-min px-2 py-px rounded-xl"
  style="font-size: 12px;"
  v-motion
  :initial="{ x: 244+65, opacity: 0, transition: {x: {mass: 1, delay: 50}} }" 
  :click-6="{ x: 244+65, opacity: 1 }"
  :click-8="{ x: 244-65   , opacity: 1 }"
  :click-10="{ x: 244-65*3   , opacity: 1 }"
>
  mask1
</div>

<div
  class="container bg-[var(--red)] w-min px-2 py-px rounded-xl"
  style="font-size: 12px;"
  v-motion
  :initial="{ x: 244, opacity: 0, y: '-100%', transition: {mass: 1.25} }" 
  :click-6="{ x: 244, opacity: 1 }"
  :click-8="{ x: 244-65*2, opacity: 1 }"
  :click-10="{ x: 244-65*4, opacity: 1 }"
>
  mask2
</div>

<span v-click='11'></span>

---

layout: two-cols
layoutClass: gap-16

---

<h1 v-if="$clicks<=7">Solution (1)</h1>
<h1 v-else>Solution (2)</h1>

Pseudocode 😃

````md magic-move {lines: true, at: 8}
```py
x = int(input())

res = 0
mask1 = 0
mask2 = 1
for i in range(?):
  bit1 = x & mask1
  bit2 = x & mask2
  res |= (bit1 << ?) | (bit2 >> ?)

  mask1 = mask1 << ??
  mask2 = mask2 << ??
```

```py {*|2,3,4,5|7|*}
x = int(input())

mask1 = 0b010101
mask2 = 0b101010
bits1 = x & mask1
bits2 = x & mask2

res = (bits1 << 1) | (bits2 >> 1)
```
````

::right::

<style>
  div.container {
    display: flex;
    gap: 50px;
    font-size: 1.5rem;
    /* span {
      width: 32px;
    } */
    span:nth-child(even){
      color: var(--comment);
    }
    span:nth-child(odd){
      color: var(--red);
    }
  }
</style>

<v-clicks hide at="7" depth="2" every="10">

## Example: 13

  <div
    class="container mt-32px"
  >
    <span v-motion :initial="{ x: 0 }" :click-6="{ x: 64 }">0</span>
    <span v-motion :initial="{ x: 0 }" :click-6="{ x: -64 }">0</span>
    <span v-motion :initial="{ x: 0 }" :click-4="{ x: 64 }">1</span>
    <span v-motion :initial="{ x: 0 }" :click-4="{ x: -64 }">1</span>
    <span v-motion :initial="{ x: 0 }" :click-2="{ x: 64 }">0</span>
    <span v-motion :initial="{ x: 0 }" :click-2="{ x: -64 }">1</span>
  </div>

  <div
    class="container bg-[var(--comment)] w-min px-2 py-px rounded-xl"
    style="font-size: 12px;"
    v-motion
    :initial="{ x: 244-65*3, opacity: 1, transition: {x: {mass: 1, delay: 50}} }" 
    :enter="{ x: 244+65, opacity: 1, transition: {x: {mass: 1, delay: 50}} }" 
    :click-1="{ x: 244+65, opacity: 1 }"
    :click-3="{ x: 244-65   , opacity: 1 }"
    :click-5="{ x: 244-65*3   , opacity: 1 }"
  >
    mask1
  </div>

  <div
    class="container bg-[var(--red)] w-min px-2 py-px rounded-xl"
    style="font-size: 12px;"
    v-motion
    :initial="{ x: 244-65*4, opacity: 1, y: '-100%', transition: {mass: 1.25} }" 
    :enter="{ x: 244, opacity: 1, y: '-100%', transition: {mass: 1.25} }" 
    :click-1="{ x: 244, opacity: 1 }"
    :click-3="{ x: 244-65*2, opacity: 1 }"
    :click-5="{ x: 244-65*4, opacity: 1 }"
  >
    mask2
  </div>
</v-clicks>

<!-- <span v-click='7'></span> -->

---

# Trick: hex

-   上頁的 `mask1` 只有 6 位，那如果是 32 位呢？

## Hex

-   1 個 hex = 4 bits
-   e.g. `0xA` = `0b1010`, `0x5` = `0b0101`, `0xAAAA = 0b1010101010101010`

<style>
  tbody{
    tr {
      td:nth-child(1) {
        font-size: 0.9rem;
      }
    }
  }
</style>

|       | 0x0 | 0x1 | 0x2 | 0x3 | 0x4 | 0x5 | 0x6 | 0x7 | 0x8 | 0x9 | 0xA | 0xB | 0xC | 0xD | 0xE | 0xF |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $2^0$ | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 1   | 0   | 1   |
| $2^1$ | 0   | 0   | 1   | 1   | 0   | 0   | 1   | 1   | 0   | 0   | 1   | 1   | 0   | 0   | 1   | 1   |
| $2^2$ | 0   | 0   | 0   | 0   | 1   | 1   | 1   | 1   | 0   | 0   | 0   | 0   | 1   | 1   | 1   | 1   |
| $2^3$ | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |

---

class: text-center
layout: center

# vertically center?

---

# The end 🎉

### Group 20

<!--
  <kbd style="font-size: 1rem; line-height:1.35rem;">B10401006 洪愷希</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem;">B12505047 陳澤諒</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem;">B11801005 何宗蕘</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem;">R13944053 温文安</kbd>
  <kbd style="font-size: 1rem; line-height:1.35rem;">B12902090 張玉慧</kbd> -->

<!-- <confetti duration="3000"></confetti> -->

<confetti-new></confetti-new>

<!-- <orbit>
HELLO
</orbit> -->
