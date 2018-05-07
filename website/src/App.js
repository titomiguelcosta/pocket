import React, { Component } from 'react';
import logo from './logo.svg';
import { Button } from 'reactstrap';
import { TabExample } from './Tabs.js';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Pocket</h1>
          <p>Scripts for currency exchange. Determine rates. Calculate balance.</p>
        </header>
        <TabExample />
      </div>
    );
  }
}

export default App;
