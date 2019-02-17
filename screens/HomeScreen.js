import React from 'react';
import {
  Image,
  Platform,
  ScrollView,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { WebBrowser } from 'expo';
// import { command } from 'node-run-cmd';
import { MonoText } from '../components/StyledText';

export default class HomeScreen extends React.Component {
  static navigationOptions = {
    header: null,
  };

  render() {
    // var nrc = require('node-run-cmd')
    return (
      <View style={styles.container}>
        <ScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
          <View style={styles.welcomeContainer}>
            <Image
              source={
                __DEV__
                  ? require('../assets/images/capitalOneLogo.png')
                  : require('../assets/images/robot-prod.png')
              }
              style={styles.welcomeImage}
            />
          </View>
        
          <View style={styles.getStartedContainer}>

            <Text style={styles.getStartedText}>Hi, {this._getName()}</Text>
            <Text> </Text>
            <Text>Your accounts-</Text>
          </View>

        <View style={styles.tabBarInfoContainer}>
          <View style={styles.moneyView}>
            <Text style={styles.tabBarInfoText}>Checking Balance:</Text>
            <Text style={styles.tabBarBalance}>$ {this._getCheckingBal()}</Text>
          </View>
          <Text style={styles.tabBarName}>Account # ...{this._getLastFour()}</Text>
        </View>

        <View style={styles.tabBarInfoContainer2}>
          <View style={styles.moneyView}>
            <Text style={styles.tabBarInfoText}>Credit Balance:</Text>
            <Text style={styles.tabBarBalance}>$ {this._getCreditBal()}</Text>
          </View>
          <Text style={styles.tabBarName}>Account # ...{this._getLastFour()}</Text>
        </View>

        </ScrollView>
      </View>
    );
  }

  _getName() {
    return ("Terry Keffer");
  }

  _getCheckingBal() {
    return 20;
  }

  _getCreditBal() {
    return 35;
  }

  _getLastFour() {
    return "3d76";
  }

}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  developmentModeText: {
    marginBottom: 20,
    color: 'rgba(0,0,0,0.4)',
    fontSize: 14,
    lineHeight: 19,
    textAlign: 'center',
  },
  contentContainer: {
    paddingTop: 30,
  },
  welcomeContainer: {
    alignItems: 'center',
    marginTop: 10,
    marginBottom: 20,
  },
  welcomeImage: {
    width: 100,
    height: 80,
    resizeMode: 'contain',
    marginTop: 3,
    marginLeft: -10,
  },
  getStartedContainer: {
    alignItems: 'flex-start',
    marginHorizontal: 50,
  },
  getStartedText: {
    fontSize: 28,
    color: '#000',
    lineHeight: 28,
    textAlign: 'center',
  },
  tabBarInfoContainer: {
    flex: 1,
    position: 'absolute',
    left: 20,
    right: 20,
    top: 225,
    ...Platform.select({
      ios: {
        shadowColor: '#004977',
        shadowOffset: { height: -3 },
        shadowOpacity: 0.5,
        shadowRadius: 3,
      },
      android: {
        elevation: 20,
      },
    }),
    backgroundColor: '#fbfbfb',
    paddingVertical: 20,
  },
  tabBarInfoContainer2: {
    position: 'absolute',
    left: 20,
    right: 20,
    top: 340,
    ...Platform.select({
      ios: {
        shadowColor: '#004977',
        shadowOffset: { height: -3 },
        shadowOpacity: 0.5,
        shadowRadius: 3,
      },
      android: {
        elevation: 20,
      },
    }),
    backgroundColor: '#fbfbfb',
    paddingVertical: 20,
  },
  tabBarInfoText: {
    fontSize: 20,
    paddingHorizontal: 10,
    color: 'rgba(96,100,109, 1)',
    textAlign: 'center',
  },
  tabBarName: {
    fontSize: 15,
    paddingHorizontal: 10,
    color: 'rgba(96,100,109, 1)',
    textAlign: 'center',
    alignSelf: 'flex-start',
  },
  tabBarBalance: {
    fontSize: 30,
    paddingHorizontal: 10,
    color: '#000',
    // alignSelf: 'flex-end',
  },
  helpContainer: {
    marginTop: 15,
    alignItems: 'center',
  },
  helpLink: {
    paddingVertical: 15,
  },
  helpLinkText: {
    fontSize: 14,
    color: '#2e78b7',
  },
  moneyView: {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
});
