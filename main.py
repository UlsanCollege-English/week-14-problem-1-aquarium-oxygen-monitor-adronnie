def max_window_sum(readings, k):
    # --- Validate inputs ---
    if not readings:
        raise ValueError("readings cannot be empty")

    if k <= 0:
        raise ValueError("k must be positive")

    if k > len(readings):
        raise ValueError("k cannot be larger than number of readings")

    # --- Compute first window ---
    window_sum = sum(readings[:k])
    max_sum = window_sum

    # --- Slide window across the list ---
    for i in range(k, len(readings)):
        window_sum += readings[i] - readings[i - k]
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum