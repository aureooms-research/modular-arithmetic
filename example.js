const add = (u,v) => {
    const t = (u+v) | 0;
    return ((t & 65535) + (t >> 16)) | 0;
};

const sub = (u,v) => {
    const t = (u-v) | 0;
    return ((t & 65535) + (t >> 16)) | 0;
};

const mul = (u,v) => {
	const t = Math.imul(u,v);
	return add(t & 65535, t >>> 16);
};

console.assert(add(0,-1) === 0xfffe);
console.assert(add(0xffff,-1) === 0xfffe);
console.assert(add(0,-2) === 0xfffd);
console.assert(add(0xffff,-2) === 0xfffd);
console.assert(add(10,-12) === 0xfffd);
console.assert(sub(1, 0xffff) === 1);
console.assert(sub(0xffff, 0xffff) === 0 || sub(0xffff, 0xffff) === 0xffff);
console.assert(sub(0xffff, 0) === 0 || sub(0xffff, 0) === 0xffff);
console.assert(sub(0, 0xffff) === 0 || sub(0, 0xffff) === 0xffff);
console.assert(mul(0xffff, 0xffff) === 0 || mul(0xffff, 0xffff) === 0xffff, 'mul');
