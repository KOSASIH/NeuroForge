import React, { useState } from 'react';
import { View, Text, Image } from 'react-native';

const Simulation2 = () => {
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
      <Image
        source={require('../assets/brain.png')}
        style={{ width: 200, height: 200 }}
      />
    </View>
  );
};

export default Simulation2;
