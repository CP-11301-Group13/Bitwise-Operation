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

# Bitwise Operations Quiz

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
# layout: two-cols
# layoutClass: gap-16
# transition: none
---

# Solution (1)

Pseudocode 😃

````md magic-move {lines: true}
```c {*|4,5|7,8|9|11,12|*}
for (int i = 0; 2 * i * k < MAX_BITS; i++) 
  mask_low |= mask_unit << 2 * i * k;
for (int i = 0; (2 * i + 1) * k < MAX_BITS; i++)
  mask_high |= mask_unit << (2 * i + 1) * k;

for (int i = 0; i < n; i++) {
    int res_high = arr[i] & mask_high;
    int res_low = arr[i] & mask_low 
    unsigned int res = (res_high >> k) | (res_low << k);
    
    printf("%u%c", res, " \n"[i == n - 1]);
}
```
````


---

# Solution (2)

````md magic-move {lines: true}
```c {*|4,5|7,8|9|11,12|*}
unsigned int mask_unit = (1 << k) - 1;

for (int i = 0; i < n; i++) {
    unsigned int res = 0, origin = arr[i], mask = mask_unit;
    for (int i = 0; i < MAX_BITS; i += 2 * k) {
        unsigned int low = origin & mask;
        mask <<= k;
        unsigned int high = origin & mask;
        mask <<= k;
        res |= (low << k) | (high >> k);
    }
    // print_bins(arr[i]);
    // print_bins(res);
    printf("%u%c", res, " \n"[i == n - 1]);
}
```
````

---
layout: two-cols
layoutClass: gap-16
# transition: none
---

# Left

This shows on the left

::right::

# Right

This shows on the right