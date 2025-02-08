import { StyleSheet, Image, View, ScrollView } from 'react-native';
import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import { LinearGradient } from 'expo-linear-gradient';

export default function ProfilePage() {
  return (
    <ScrollView contentContainerStyle={styles.scrollContainer}>
      <LinearGradient
        colors={['#1E1E1E', '#121212']}
        style={styles.gradientBackground}
      >
        <View style={styles.container}>
          <ThemedView style={styles.header}>
            <Image
              source={require('@/assets/images/icon.png')} // Replace with actual image path
              style={styles.profileImage}
            />
            <ThemedText type="title" style={styles.username}>
              John Doe
            </ThemedText>
            <ThemedText style={styles.userHandle}>@johndoe</ThemedText>
          </ThemedView>

          <ThemedView style={styles.bioContainer}>
            <ThemedText style={styles.bioText}>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </ThemedText>
          </ThemedView>

          <ThemedView style={styles.detailsContainer}>
            <View style={styles.detailItem}>
              <ThemedText type="defaultSemiBold" style={styles.detailLabel}>
                Email:
              </ThemedText>
              <ThemedText style={styles.detailValue}>johndoe@example.com</ThemedText>
            </View>
            <View style={styles.detailItem}>
              <ThemedText type="defaultSemiBold" style={styles.detailLabel}>
                Location:
              </ThemedText>
              <ThemedText style={styles.detailValue}>San Francisco, CA</ThemedText>
            </View>
          </ThemedView>
        </View>
      </LinearGradient>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  scrollContainer: {
    flexGrow: 1,
  },
  gradientBackground: {
    flex: 1,
  },
  container: {
    flex: 1,
    padding: 24,
  },
  header: {
    alignItems: 'center',
    marginBottom: 24,
  },
  profileImage: {
    width: 150,
    height: 150,
    borderRadius: 75,
    marginBottom: 16,
    borderWidth: 3,
    borderColor: '#FFFFFF',
  },
  username: {
    fontSize: 28,
    fontWeight: 'bold',
    color: 'white',
    marginBottom: 4,
  },
  userHandle: {
    fontSize: 16,
    color: '#A0A0A0',
  },
  bioContainer: {
    backgroundColor: '#2C2C2C',
    borderRadius: 12,
    padding: 16,
    marginBottom: 24,
  },
  bioText: {
    fontSize: 16,
    color: '#E0E0E0',
    lineHeight: 24,
  },
  detailsContainer: {
    backgroundColor: '#2C2C2C',
    borderRadius: 12,
    padding: 16,
  },
  detailItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  detailLabel: {
    fontSize: 16,
    color: '#E0E0E0',
    fontWeight: '600',
  },
  detailValue: {
    fontSize: 16,
    color: '#A0A0A0',
  },
});