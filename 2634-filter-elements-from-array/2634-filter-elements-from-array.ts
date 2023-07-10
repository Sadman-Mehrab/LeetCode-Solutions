function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
    const ret: number[] = [];
    for (let i =0;i<arr.length;i++)
        if(fn(arr[i],i))
            ret.push(arr[i]);
    return ret;
};