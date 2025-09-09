async function handleFileUpload(event) {
    const file = event.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("http://127.0.0.1:8000/tryon", {
            method: "POST",
            body: formData,
        });
        const data = await response.json();
        console.log(data);

        const resultImg = document.getElementById("resultImg");
        resultImg.src = data.generated_image;
        resultImg.style.display = "block";
    } catch (err) {
        console.error("Error uploading file:", err);
    }
}
