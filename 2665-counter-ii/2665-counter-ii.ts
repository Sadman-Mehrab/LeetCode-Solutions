type ReturnObj = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): ReturnObj {
    let val: number = init;
    const increment = (): number =>{
        return ++val;
    }
    const decrement = (): number =>{
        return --val;
    }
    const reset = (): number =>{
        val = init;
        return val;
    }
    
    return {increment,decrement, reset};
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */