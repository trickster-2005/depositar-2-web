const lightbox = GLightbox({
  selector: ".glightbox",
  height: "150px",
});

const selector = document.getElementById("dataset-filter");
selector.addEventListener("change", () => {
  const selected = selector.value;
  const items = document.querySelectorAll(".masonry-item");
  items.forEach((item) => {
    const dataset = item.getAttribute("data-dataset");
    if (selected === "all" || dataset === selected) {
      item.style.display = "block";
    } else {
      item.style.display = "none";
    }
  });
});
