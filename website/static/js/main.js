document.addEventListener('DOMContentLoaded', () => {
    const carouselReel = document.querySelector('.carousel .reel');
    const carouselForward = document.querySelector('.carousel .forward');
    const carouselBackward = document.querySelector('.carousel .backward');

    if (carouselReel && carouselForward && carouselBackward) {
        const scrollAmount = 320;

        carouselForward.addEventListener('click', () => {
            carouselReel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        });

        carouselBackward.addEventListener('click', () => {
            carouselReel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        });
    }
});
