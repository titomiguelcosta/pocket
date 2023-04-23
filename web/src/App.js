import React, { Component } from 'react';
import { Tabs } from './Tabs.js';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Pocket</h1>
          <p>Scripts for forex (foreign exchange). Check rates. Calculate balance. Determine fees.</p>
        </header>
        <Tabs />
      </div>
    );
  }
}

export default App;
