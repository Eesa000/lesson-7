def square_it_out(start, end):
    squares = []

    # Create list of square values
    for num in range(start, end + 1):
        squares.append(num ** 2)

    # Separate even and odd squares
    even_squares = []
    odd_squares = []
