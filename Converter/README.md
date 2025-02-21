# Converter Notes
## Plan
- ability to change between celsius and farenheit, metric and imperial
- ability to take input
- 16 cm = 2 inches (inside joke funny to me and 1 friend)

## What I did
### Farenheit to Celsius:
Tested following code in sandbox:

```
let f = 99;
let c = (f-32)5/9;
console.log(c);
```

Returned "SyntaxError: unexpected token: numeric literal"
Tried again with () and "*" as below:

```
let f = 99;
let c = ((f-32)*5)/9;
console.log(c);
```

Returned "37.22222222222222"
Looked up "99 farenheit to celsius" and got "37.2"
Yay!

### Adding Prompt
Checked *Eloquent JS* for "prompt" function
Tested in sandbox "https://eloquentjavascript.net/code/"

Tested following code in sandbox:
```
let f = prompt("enter farenheit value");
let c = ((f-32)*5)/9;
console.log(c);
```

Returned "37.222222"
Yay!

### Adding switch between Farenheit and Celsius
Tried following in sandbox:

```
let tempType = prompt("enter Farenheit or Celsius");
if tempType == "Farenheit" || "farenheit" {
   let f = prompt("enter value");
   let c = ((f-32)*5)/9;
   console.log(c);
}
else {
	console.log("Sorry, idk how to do that"");
}
```

Forgot () around condition :( trag

```
let tempType = prompt("enter Farenheit or Celsius");
if (tempType == "Farenheit" || "farenheit") {
   let f = prompt("enter value");
   let c = ((f-32)*5)/9;
   console.log(c);
}
else {
	console.log("Sorry, idk how to do that");
}
```

Seems to think it's farenheit no matter what :/
Took out "|| 'farenheit'" and it's working now
Changed to "|| if tempType == 'farenheit'" and that works lmao

looked up celsius to farenheit conversion and apparently i've been spelling farenheit wrong this whole time

thanks wikihow for c to f formula: https://www.wikihow.com/Convert-Celsius-(%C2%B0C)-to-Fahrenheit-(%C2%B0F)
f=c*(9/5)+32

Tested following in sandbox w/ "celsius" and "7" inputs

```
let tempType = prompt("enter Farenheit or Celsius");
if (tempType === "Farenheit" || tempType === "farenheit") {
   let f = prompt("enter value");
   let c = ((f-32)*5)/9;
   console.log(c);
}
else {
  let c = prompt("enter value");
  let f = c*(9/5)+32;
  console.log(f);
}
```

Returned 44.6
Looked it up and got the same

### adding centimeters and inches
formula from "https://www.checkyourmath.com/convert/length/cm_inches.php"

Tested following in sandbox w "cm" and "8", returned 3.149606299212598

```
let tempType = prompt("convert FROM one of the following: Fahrenheit, Celsius, cm, or in");
if (tempType === "Fahrenheit" || tempType === "fahrenheit") {
   let f = prompt("enter value");
   let c = ((f-32)*5)/9;
   console.log(c);
}
if (tempType === "Celsius" || tempType === "celsius") {
  let c = prompt("enter value");
  let f = c*(9/5)+32;
  console.log(f);
}

if (tempType === "cm") {
  let cm = prompt("enter value");
  let inch = cm/2.54;
  console.log(inch);
}

if (tempType === "in") {
  let inch = prompt("enter value");
  let cm = inch*2.54;
  console.log(cm);
}
```

### adding inside joke and text

Tested following in sandbox, returned "2 inches"

```
let tempType = prompt("convert FROM one of the following: Fahrenheit, Celsius, cm, or in");
if (tempType === "Fahrenheit" || tempType === "fahrenheit") {
   let f = prompt("enter value");
   let c = ((f-32)*5)/9;
   console.log(c + "C");
}
if (tempType === "Celsius" || tempType === "celsius") {
  let c = prompt("enter value");
  let f = c*(9/5)+32;
  console.log(f + "F");
}

if (tempType === "cm") {
  let cm = prompt("enter value");
  if (cm === "16") {
    console.log("2 inches");
  }
  else {
  let inch = cm/2.54;
  console.log(inch + "in");
  }
}

if (tempType === "in") {
  let inch = prompt("enter value");
  let cm = inch*2.54;
  console.log(cm + "cm");
}
```









