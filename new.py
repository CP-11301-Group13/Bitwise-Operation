import subprocess
import resource

def get_memory_usage():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

# Get initial memory usage
initial_memory = get_memory_usage()
print(f"Initial memory usage: {initial_memory} KB")

# Run a subprocess
subprocess.run(["ls", "-l"])

# Get final memory usage
final_memory = get_memory_usage()
print(f"Final memory usage: {final_memory} KB")

# Calculate and print the difference
memory_difference = final_memory - initial_memory
print(f"Memory usage difference: {memory_difference} KB")