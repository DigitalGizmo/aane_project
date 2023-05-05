// const slimpopElement = document.getElementById("slimpop-overlay")

htmx.on("htmx:afterSwap", (e) => {
    console.log("inafterSwap, target id: " + e.detail.target.id)
    if (e.detail.target.id == "slimpop-container") {
        document.getElementById("slimpop-overlay").classList.remove("hidden");
        // document.getElementById("slimpop-overlay").classList.add("unhidden");

    }
})

htmx.on("htmx:beforeSwap", (e) => {
    console.log("got to close")
    if (e.detail.target.id == "close-button") {
        document.getElementById("slimpop-overlay").classList.add("hidden");
    }
})