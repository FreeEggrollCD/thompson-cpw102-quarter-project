# Product Requirements Document


## Problem

There don't seem to be a lot of AIO benchmarking tools out there. The ones that do exist are also not very simple or lightweight.
This AIO benchmarking tool aims to be as simple as the user needs with varying levels of verbosity.

## Desired outcome

I believe that the aspect users would find the most desireable would be the customizeable verbosity of the benchmark output.
Not everyone is concerned with every aspect of the hardware, sometimes all you want to know is your disks read/write speed.
Maybe you only wanna know the performance of a single CPU core.

## Scope

This app will cover all major benchmarks of a computer: CPU, Memory, and GPU along with Disk R/W speeds.

## Out of Scope

When it comes to benchmarking you don't need fancy graphs unless you want to plot over time.
That only comes into play for Disk R/W speeds and maybe CPU temp. But there's already software dedicated those cases that
already do a great job and are already lightweight because of the singular scope they cover.

## Requirements

The program needs accurately benchmark the hardware. Otherwise it's of no use to anyone.

### The product must

- Accurately benchmark the hardware.
- Take into account the user's desired verbosity

### The product should

- Not benchmark all hardware at the same time.

### The product could

- Output benchmark results to a text file or CSV.