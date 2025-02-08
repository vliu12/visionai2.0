import { Image, Platform, View, Text, TouchableWithoutFeedback, Alert, StyleSheet } from 'react-native';
import React, { useState } from 'react';
import { useNavigation } from '@react-navigation/native';
import api from '@/api/api';

const AppComponent = () => {
  const [navigationMode, setIsTrue] = useState(false);
  const navigation = useNavigation();
  
  const startNavigation = () => {
    try {
      const response = api.get('/navigate');
    } catch (error) {
      console.log("ERROR", error);
    }
  }

  const startDet = () => {
    setIsTrue(true);
    try {
      const response = api.get('/classify');
    } catch (error) {
      console.log("ERROR", error);
    }
  };

  const handlePress = () => {
    console.log("handlePress Started");
    startDet(); // Call startDet function
    startNavigation(); // Call startNavigation function
  };

  const stopDet = () => {
    try {
      const response = api.get('/stopClassify');
    } catch (error) {
      console.log("ERROR", error);
    }
  };

  return (
    <TouchableWithoutFeedback onPress={handlePress}>
        <View style={styles.container}>
          <Text style={[styles.text, {color: navigationMode ? "black" : "white"}]}>Welcome to SightBridge.</Text>
        </View>
      </TouchableWithoutFeedback>
  );
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'black',
  },
  text: {
    color: 'white',
    fontSize: 24,
    fontWeight: 'bold',
  },
});

export default AppComponent;
