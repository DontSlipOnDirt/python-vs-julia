using LinearAlgebra, Zygote, BenchmarkTools

function matrix_mult_benchmark(A, B)
    return minimum(@benchmark A * B).time / 1e6  # Convert to milliseconds
end

function elementwise_exp_benchmark(X)
    return minimum(@benchmark exp.(X)).time / 1e6
end

function gradient_benchmark(x)
    f = x -> sum(x.^3 + 2x.^2 + 5x)
    return minimum(@benchmark gradient($f, $x)).time / 1e6
end

# testing in julia
# A = rand(1000, 1000)
# B = rand(1000, 1000)

# X = rand(1_000_000)

# x = collect(range(-100, 100, length=100000))

# println(matrix_mult_benchmark(A, B), " ms")
# println(elementwise_exp_benchmark(X), " ms")
# println(gradient_benchmark(x), " ms")