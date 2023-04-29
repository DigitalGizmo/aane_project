// const slimpopElement = document.getElementById("slimpop-overlay")

htmx.on("htmx:afterSwap", (e) => {
    if (e.detail.target.id == "slimpop-container") {
        console.log("got to afterSwap")
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