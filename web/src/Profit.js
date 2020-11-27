import React from 'react';
import { Button, Form, FormGroup, Label, Input, Col, Alert } from 'reactstrap';
import { Currency } from './Currency';

export class Profit extends React.Component {
  constructor(props) {
    super(props);
    this.url ='https://pocket.titomiguelcosta.com'
    this.state = {
        description: null,
        source: 'EUR',
        target: 'NZD',
        profit: null,
        transferred: null,
        cashed: null
    }
  }

  handleSubmit(e) {
    e.preventDefault()
    this.setState({description: null})
    let endpoint = ''
    if (this.state.cashed) {
        endpoint = `${this.state.transferred}/${this.state.profit}/${this.state.cashed}/${this.state.source}/${this.state.target}`
    } else {
        endpoint = `${this.state.transferred}/${this.state.profit}/${this.state.source}/${this.state.target}`
    }

    fetch(`${this.url}/profit/${endpoint}`)
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

            <FormGroup row>
                <Label for="profitProfit" sm={4}>Profit *</Label>
                <Col sm={2}>
                    <Input type="currency" id="profitProfit" onChange={(e) => this.handleCurrency(e, 'profit')} />
                </Col>
            </FormGroup>

            <FormGroup row>
                <Label for="profitTransferred" sm={4}>Transferred *</Label>
                <Col sm={2}>
                    <Input type="currency" id="profitTransferred" onChange={(e) => this.handleCurrency(e, 'transferred')} />
                </Col>
            </FormGroup>

            <FormGroup row>
                <Label for="profitCashed" sm={4}>Cashed</Label>
                <Col sm={2}>
                    <Input type="currency" id="profitCashed" onChange={(e) => this.handleCurrency(e, 'cashed')} />
                </Col>
            </FormGroup>

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