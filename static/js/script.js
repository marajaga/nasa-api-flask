// ScrollMagic Rocket
const path = [{ x: 0, y: -5000 }];

const plane = document.getElementById('rocket');

const TL = new TimelineMax();

TL
    .to(rocket, 2.5, { bezier: { values: path } });


const controller = new ScrollMagic.Controller();

const scene = new ScrollMagic.Scene({
    triggerElement: '#trigger',
    duration: 3000,
    triggerHook: 0.4
})

    .setPin(rocket)
    .setTween(TL)
    .addTo(controller);


