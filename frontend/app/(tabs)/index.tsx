import { Image, StyleSheet, Platform, View, Text, Button } from 'react-native';


import { HelloWave } from '@/components/HelloWave';
import ParallaxScrollView from '@/components/ParallaxScrollView';
import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import api from '@/api/api'

export default function HomeScreen() {
  const handlePress = () => {
    try {
      const response = api.get('/classify')
    } catch (error) {
      
    }
  };
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Welcome to SightBridge.</Text>
      <Text style={styles.text}>Sight through computer vision.</Text>
      <Button
        title="Click this to Start Detection"
        onPress={handlePress}
        accessibilityLabel="Start object detection"
      />
    </View>
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


