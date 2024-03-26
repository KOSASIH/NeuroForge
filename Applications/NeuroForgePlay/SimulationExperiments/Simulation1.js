import React, { useState } from 'react';
import { View, Text } from 'react-native';

const Simulation1 = () => {
  const [buttonState, setButtonState] = useState('Press to Start');

  const handlePress = () => {
    setButtonState('Running...');

    // Simulation code goes here

    setTimeout(() => {
      setButtonState('Simulation Finished');
    }, 3000);
  };

  return (
    <View>
      <Text onPress={handlePress}>{buttonState}</Text>
    </View>
  );
};

export default Simulation1;
