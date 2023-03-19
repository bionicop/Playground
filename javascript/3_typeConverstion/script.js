console.group('String to Number');
let a = '100';
let aa = 'hmm';
a = parseInt(a);
aa = parseInt(aa);
// a =+ a;
// a = Number(a);

console.log(a, typeof a);
console.log(aa, typeof aa);
console.groupEnd();


console.group('Number to String');
let b = 100;
//b = b.toString();
b = String(b);

console.log(b, typeof b);
console.groupEnd();


console.group('String to Decimal');
let c = '100.69';
c = parseFloat(c);

console.log(c, typeof c);
console.groupEnd();


console.group('Number to Boolean');
let d = 0;
d = Boolean(d);

console.log(d, typeof d);
console.groupEnd();
