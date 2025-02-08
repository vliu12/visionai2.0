import { StyleSheet, Image, View } from 'react-native';

export default function ProfilePage() {
  return (
    <View style={styles.container}>
      <Image 
        source={require('@/assets/images/exclaim.png')} 
        style={styles.imageE}
      />
      <Image 
        source={require('@/assets/images/triangle.png')} 
        style={styles.imageT}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'red',
    justifyContent: 'center',
    alignItems: 'center',
    position: 'relative',
  },
  imageT: {
    position: 'absolute',
    width: 120,
    height: 100, 
  },
  imageE: {
    width: 10,
    height: 50, 
  }
});
