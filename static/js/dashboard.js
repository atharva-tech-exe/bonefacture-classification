document.addEventListener("DOMContentLoaded", () => {

```
const uploadZone = document.querySelector(".upload-zone");
const fileInput = document.querySelector('input[type="file"]');

if (uploadZone && fileInput) {

    uploadZone.addEventListener("dragover", (e) => {
        e.preventDefault();
        uploadZone.classList.add("dragover");
    });

    uploadZone.addEventListener("dragleave", () => {
        uploadZone.classList.remove("dragover");
    });

    uploadZone.addEventListener("drop", (e) => {
        e.preventDefault();
        uploadZone.classList.remove("dragover");

        if (e.dataTransfer.files.length > 0) {
            fileInput.files = e.dataTransfer.files;
        }
    });
}

const themeButton = document.getElementById("themeToggle");

if (themeButton) {

    themeButton.addEventListener("click", () => {

        document.body.classList.toggle("light-mode");

        if (document.body.classList.contains("light-mode")) {

            document.body.style.background = "#f8fafc";
            document.body.style.color = "#111827";

        } else {

            document.body.style.background = "#0B0F19";
            document.body.style.color = "#F8FAFC";
        }

    });

}
```

});
