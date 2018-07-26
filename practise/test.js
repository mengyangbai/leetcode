// Complete the maxLength function below.
function maxLength(a, k) {
    let sub_start = 0;
    let sub_end = 0;
    let sub_sum = 0;
    let max_len = 0;
    for (let i = 0; i < a.length; i++) {
        sub_end += 1;
        sub_sum += a[i];
        while (sub_sum > k) {
            sub_sum -= a[sub_start];
            sub_start += 1;
        }

        max_len = Math.max(max_len, sub_end - sub_start);
    }

    return max_len;
}

console.log(maxLength([2, 3, 4, 5]))