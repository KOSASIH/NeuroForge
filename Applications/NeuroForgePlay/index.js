import React from 'react';
import { View } from 'react-native';
import SimulationExperiments from '../Simulation_Experiments/index';
import NeuromorphicHardwareDesigns from '../Neuromorphic_Hardware_Designs/index';
import CognitiveComputingAlgorithms from '../Cognitive_Computing_Algorithms/index';
import BrainInspiredArchitectures from '../Brain_Inspired_Architectures/index';

const NeuroForgePlay = () => {
  return (
    <View>
      <SimulationExperiments />
      <NeuromorphicHardwareDesigns />
      <CognitiveComputingAlgorithms />
      <BrainInspiredArchitectures />
    </View>
  );
};

export default NeuroForgePlay;
