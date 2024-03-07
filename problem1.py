import math as m


def pi_LiuHui(epsilon):
    """
    Calculates pi using Liu Hui's formula

    :param epsilon: accuracy of the pi returned
    :return: approximation of the pi returned
    """
    n_sides = 6
    side_len = 1
    pi_approx = n_sides * m.sqrt(1 - m.sqrt(1 - (side_len / 2) ** 2))

    while abs(pi_approx - m.pi) > epsilon:
        n_sides *= 2    # double number of sides
        side_len = m.sqrt(2 - 2 * m.sqrt(1 - (side_len / 2) ** 2))  # Calculate new side length
        pi_approx = n_sides * side_len / 2  # Update pi approximation

        # Break if n_sides becomes too large to handle
        if n_sides > 1e16:
            break

    return pi_approx



