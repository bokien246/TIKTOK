const imageSelector = document.getElementById('imageSelector');
const imageContainer = document.getElementById('imageContainer');

imageSelector.addEventListener('change', function() {
    const value = this.value;
    let imagePath = '';
    let linkPath = '';

    switch (value) {
        case 'image1':
            imagePath = 'img/1.jpg';
            break;
        case 'image2':
            imagePath = 'img/2.avif';
            break;
        case 'image3':
            imagePath = 'img/3.png';
            break;
        case 'image4':
            linkPath = 'index2.html';
            break;
        default:
            imagePath = '';
    }

    if (imagePath) {
        imageContainer.innerHTML = `<img src="${imagePath}" alt="${value}">`;
    } else if (linkPath) {
        window.location.href = linkPath;
    } else {
        imageContainer.innerHTML = '';
    }
});
