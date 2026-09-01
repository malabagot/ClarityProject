const wakeup_hh = document.getElementById("wakeup_hh");
const wakeup_mm = document.getElementById("wakeup_mm");
const wakeup_box = document.getElementById("wakeup")

const fallasleep_hh = document.getElementById("fallasleep_hh");
const fallasleep_mm = document.getElementById("fallasleep_mm");
const fallasleep_box = document.getElementById("fallasleep")

let wakeup_entered = false;
let fallasleep_entered = false;

//box being the name of the current variable the for loop is looking at
[wakeup_hh, wakeup_mm, fallasleep_hh, fallasleep_mm].forEach(box => {
box.addEventListener("input", () => {
    box.value = box.value.replace(/[^0-9]/g, "").slice(0, 2);
    console.log("corrected!!");


    if (box === wakeup_hh && wakeup_hh.value.length === 2) wakeup_mm.focus();
    if (box === fallasleep_hh && fallasleep_hh.value.length === 2) fallasleep_mm.focus();
});

});


wakeup_mm.addEventListener("keydown", e => {
if (e.key === "Backspace" && wakeup_mm.value === "") wakeup_hh.focus();
if (e.key === "Enter" && wakeup_mm.value.length === 2 && wakeup_hh.value.length === 2) { wakeup_entered = true; wakeup_box.style.display = "none";}
if (fallasleep_entered === true && wakeup_entered === true) {
    fetch("/sleep",{
        method: "POST",
        body: JSON.stringify({wakeup_hh: wakeup_hh.value, wakeup_mm: wakeup_mm.value, fallasleep_hh: fallasleep_hh.value, fallasleep_mm: fallasleep_mm.value}),
        headers: {"Content-Type": "application/json"},
            })};
}); 

fallasleep_mm.addEventListener("keydown", e => {
if (e.key === "Backspace" && fallasleep_mm.value === "") fallasleep_hh.focus();

if (e.key === "Enter" && fallasleep_mm.value.length === 2 && fallasleep_hh.value.length === 2) { fallasleep_entered = true; fallasleep_box.style.display = "none";}
if (fallasleep_entered === true && wakeup_entered === true) {
    fetch("/sleep",{
        method: "POST",
        body: JSON.stringify({wakeup_hh: wakeup_hh.value, wakeup_mm: wakeup_mm.value, fallasleep_hh: fallasleep_hh.value, fallasleep_mm: fallasleep_mm.value}),
        headers: {"Content-Type": "application/json"},
            })};
});


