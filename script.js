document.addEventListener('DOMContentLoaded', function() {
    const slider = document.getElementById('trust-rating');
    const sliderValue = document.getElementById('slider-value');

    slider.addEventListener('input', function() {
        sliderValue.textContent = this.value;
    });
});
