import React from 'react';
import {  ScrollView,
          StyleSheet,
          Text,
          View,
          Platform,
          Button,
        } from 'react-native';
import { ExpoLinksView } from '@expo/samples';

export default class LinksScreen extends React.Component {
  static navigationOptions = {
    title: 'Instant Bill Pay',
  };

  render() {
    return (
      <ScrollView style={styles.container}>
        <View style={styles.moneyView}>
          <Text style={styles.accountType}>Checkings</Text>
          <Text style={styles.amountText}>${this._getChecking()}</Text>
        </View>
        <View style={styles.moneyView}>
          <Text style={styles.accountType}>Credit</Text>
          <Text style={styles.amountText}>${this._getCredit()}</Text>
        </View>

        <View style={styles.line}/>

        <View style={styles.moneyView}>
          <Text style={styles.accountType}>Net Sum</Text>
          <Text style={styles.amountText}>${this._sum()}</Text>
        </View>

        {this._canPayBill()}

      </ScrollView>
    );
  }

  _getChecking() {
    return 25;
  }
  _getCredit() {
    return 30;
  }
  _sum() {
    return (this._getChecking() - this._getCredit());
  }

  _canPayBill() {
    if (this._sum() > 0) {
      const canPay = (
        <Button 
          onPress={this._buttonThing} 
          title="Pay"
          color="#fff"
          accessibilityLabel="Pay the credit card bill!"
        />
      
      );
      return (
        <View style={styles.buttonStyle}>{canPay}</View>
      );
    } else {
      return (
        <View style={styles.tabBarInfoContainer}>
          <Text style={styles.warning}>The balance of your checking account is insufficient to pay
          the total of your credit balance.
          </Text>
        </View>
      );
    }
  }
  _buttonThing = () => {
    console.log('ok')
  };
}



const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: 15,
    backgroundColor: '#fff',
  },
  amountText: {
    fontSize: 35,
  },
  accountType: {
    fontSize: 25,
  },
  moneyView: {
    marginBottom: 15,
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingHorizontal: 20,
    alignItems: 'center',
  },
  line: {
    borderBottomColor: 'rgba(96,100,109, 1)',
    borderBottomWidth: 1,
    marginHorizontal: 10,
    marginBottom: 15,
    ...Platform.select({
      ios: {
        shadowColor: 'black',
        shadowOffset: { height: -5 },
        shadowOpacity: 0.1,
        shadowRadius: 5,
      },
      android: {
        elevation: 20,
      },
    }),
  },
  tabBarInfoContainer: {
    position: 'absolute',
    left: 20,
    right: 20,
    top: 300,
    ...Platform.select({
      ios: {
        shadowColor: 'red',
        shadowOffset: { height: -3 },
        shadowOpacity: 0.5,
        shadowRadius: 4,
      },
      android: {
        elevation: 20,
      },
    }),
    alignItems: 'center',
    backgroundColor: '#fff',
    paddingVertical: 20,
    justifyContent: 'center',
  },
  buttonStyle: {
    backgroundColor: '#004977',
    marginHorizontal: 30,
    height: 60,
    fontSize: 30,
    top: 150,
    justifyContent: 'center',
    borderRadius: 30,
  },
  warning: {
    textAlign: 'center',
    color: 'rgba(96,100,109, 1)',
    padding: 10,
  }
});
