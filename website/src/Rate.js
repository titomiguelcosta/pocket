import React from 'react';
import { Button, Form, FormGroup, Label, Input, Col, Alert } from 'reactstrap';
import { Currency } from './Currency';

export class Rate extends React.Component {
  constructor(props) {
    super(props);
    this.url ='https://pocket.titomiguelcosta.com'
    this.state = {
        description: null,
        source: 'EUR',
        target: 'NZD'
    }
  }

  handleSubmit(e) {
    e.preventDefault()
    this.state.description = null
    fetch(`${this.url}/rate/${this.state.source}/${this.state.target}`)
        .then((res) => res.json())
        .then((data) => {
            this.setState({description: data.description})
        })
        .catch((error) => {
            this.setState({description: "Failed to connect."})
        })
  }

  handleCurrency(e, widget) {
    this.setState({[widget]: e.target.value})
  }

  render() {
    return (
      <div className="form">
        <Form onSubmit={(e) => this.handleSubmit(e)}>
            <Currency name="Source" field="source"  default={this.state.source} handleCurrency={this.handleCurrency.bind(this)} />
            <Currency name="Target" field="target" default={this.state.target} handleCurrency={this.handleCurrency.bind(this)} />

            <FormGroup>
                <Button>Calculate</Button>
            </FormGroup>
        </Form>
        {
            this.state.description &&
            <Alert color="dark" id="output">
                {this.state.description}
            </Alert>
        }
      </div>
    )
  }
}