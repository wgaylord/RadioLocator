import math

def powerLevel(sample):
    return 10 * math.log10((sample.real**2)+(sample.imag**2))

def averagePowerLevel(powerLevels):
        level = 0
        for x in powerLevels:
            level = level + x
        return level/(len(powerLevels)*1.0)
        
def sampleToAveragePower(samples):
        samples = samples.tolist()
        powers = []
        for x in samples:
            powers.append(powerLevel(x))
        return averagePowerLevel(powers)