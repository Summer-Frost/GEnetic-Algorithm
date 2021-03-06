# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 16:31:17 2018

@author: Shakir
"""

import random
import datetime


geneSet =' #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.'
target ='String you wanna generate'



def generate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return ''.join(genes)


def get_fitness(guess):
    return sum(1 for expected, actual in zip(target, guess)
               if expected == actual)

def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    if newGene == childGenes[index] :
          childGenes[index] = alternate 
    else:
        newGene
    return ''.join(childGenes)


def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))


random.seed()
startTime = datetime.datetime.now()
bestParent = generate_parent(len(target))
bestFitness = get_fitness(bestParent)
display(bestParent)

while True:
    child = mutate(bestParent)
    childFitness = get_fitness(child)

    if bestFitness >= childFitness:
        continue
    display(child)
    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child
