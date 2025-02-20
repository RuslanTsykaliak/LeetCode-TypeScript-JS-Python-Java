function productExceptSelf(nums: number[]): number[] {
    const length = nums.length // Total number of elements in input array
    const result: number[] = new Array(length) // Initialize an array to store the result

    // Forward pass: Calculate the product of all elements to the left of each index
    for (let i = 0, productToLeft = 1; i < length; i++) {
        result[i] = productToLeft; // Set the product (initially 1)
        productToLeft *= nums[i] // Update the productToLeft for the next index
    }

    // Backward pass: Calculate the product of all elemtents to the right of each index
    for (let i = length -1, productToRigth = 1; i >= 0; i--) {
        result[i] *= productToRigth // Multiply with the already stored product to the left
        productToRigth *= nums[i] // Update the productToRight for teh previous index
    }

    return result // Return the final result array
};