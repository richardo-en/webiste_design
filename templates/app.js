const html = document.documentElement;
const canvas = document.querySelector('.cool-anim');
const context = canvas.getContext('2d');

const currentFrame = index => (
    '20210523_091101_${index.toString().padStart(4 , '0')}.jpg'
)

const frameCount = 30;

canvas.height = 1920;
canvas.width = 1080;
const img = new Image();
img.src = currentFrame(1);
img.onload = function(){
    context.drawImage(img , 0 , 0)
}

const updateImage = index => {
    img.src = currentFrame(index)
    context.drawImage(img , 0 , 0);
}

window.addEventListener('scroll' , () =>{
    const scrollTop = html.scrollTop;
})