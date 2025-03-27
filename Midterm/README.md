# Key Bind Sounds

## The Link
https://editor.p5js.org/ZCFischthal/sketches/E_sbGlvD8

## Making It Play Sounds

From 05 Functions codealong:

```
let soundA;

function preload() {
  soundA = loadSound('thankYou.wav');
}

function setup() {
  soundA.play();
}
```

## Binding Sounds to Keys

From 05 Functions codealong:

```
let soundA;

function preload() {
  soundA = loadSound('thankYou.wav');
}

function setup() {
  createCanvas(400, 200);
  textSize(20);
  textAlign(CENTER, CENTER);
  text("Move your cursor to the 'Preview' section\nPress 'P' to play sound", width / 2, height / 2);
}

function keyPressed() {
  console.log("Key Pressed:", key);
  if (key.toLowerCase() === 'p'){
    playMySound();
  }
}

function playMySound() {
  if (soundA.isLoaded()){
    soundA.play();
    console.log("Sound A played.");
  }
  else {
    console.log("Sound A not loaded yet.")
  }
}
```

## Adding More Sounds and Keys

Original was calling separate function to play sound instead of just playing it inside the keyPressed function. That seemed way more annoying to copy/paste (bc I'd have to copy and change the keypress letters both in the "keyPressed" function and in the "playMySound" function instead of just one), so I just put everything in the "keyPressed" function instead.

```
let soundA;

function preload() {
  soundA = loadSound('thankYou.wav');
  soundB = loadSound('thankYou.wav');
  soundC = loadSound('thankYou.wav');
}

function setup() {
  createCanvas(400, 200);
  textSize(20);
  textAlign(CENTER, CENTER);
  text("Move your cursor to the 'Preview' section\nPress 'A', 'B', or 'C' to play sound", width / 2, height / 2);
}

function keyPressed() {
  console.log("Key Pressed:", key);
  if (key.toLowerCase() === 'a'){
    if (soundA.isLoaded()){
    soundA.play();
    console.log("Sound A played.");
    }
    else {
      console.log("Sound A not loaded yet.");
    }
  }
  if (key.toLowerCase() === 'b'){
    if (soundB.isLoaded()){
      soundB.play();
      console.log("Sound B played.");
    }
    else {
      console.log("Sound B not loaded yet.");
    }
  }
  if (key.toLowerCase() === 'c'){
    if (soundC.isLoaded()){
      soundC.play();
      console.log("Sound C played.");
    }
    else {
      console.log("Sound C not loaded yet.");
    }
  }
}
```

## Plan for More/Different Sounds

### Changing Sound
```
if (key === '[key name]'){
mySound = [whichever sound file loaded under preload]
}
```
added a bunch of sounds, each changed by different numbers

### Changing Pitch
Tried to find an actual pitch shifting function on the p5.js website reference and tutorials, but it took more than 5 minutes so I used ".rate" as in the functions codealong instead.
```
if (key.toLowerCase() === 'w'){
    mySound.rate(1.2);
    mySound.play();
  }
```

Mostly works, except I have the rate increasing by 0.1 per key press (so q=1, w=1.1, etc.), which doesn't work out to a whole or half step.
Increased instead by 1/12 (.083) —> half steps, still kind of out of tune
AHHHH how do i make this in tune

Everybody say *thank you reddit* my bad for not thinking about how sound actually works obv it wouldn't be a linear equation
https://www.reddit.com/r/audioengineering/comments/5wwd4r/how_to_calculate_pitch_change_from_speed_change/
s = 2t/12

Also thank you Desmos

### Visual
https://www.publicdomainpictures.net/es/view-image.php?image=44325&picture=piano-keyboard-clipart
I added the letters myself (the actual notes are not correct AT ALL apologies to those of you with perfect pitch)
Also changed the text to tell user what's actually going on
