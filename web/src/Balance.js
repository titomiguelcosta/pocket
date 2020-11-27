import React from 'react';
import { Button, Form, FormGroup, Label, Input, Col, Alert } from 'reactstrap';
import { Currency } from './Currency';

export class Balance extends React.Component {
  constructor(props) {
    super(props);
    this.url ='https://pocket.titomiguelcosta.com'
    this.state = {
        description: null,
        source: 'EUR',
        target: 'NZD',
        rate: null,
        transferred: null,
        cashed: null
    }
  }

  handleSubmit(e) {
    e.preventDefault()
    this.setState({description: null})
    let endpoint = ''
    if (this.state.rate) {
        endpoint = `${this.state.transferred}/${this.state.cashed}/${this.state.rate}/${this.state.source}/${this.state.target}`
    } else {
        endpoint = `${this.state.transferred}/${this.state.cashed}/${this.state.source}/${this.state.target}`
    }

    fetch(`${this.url}/balance/${endpoint}`)
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
                <Label for="balanceTransferred" sm={4}>Transferred *</Label>
                <Col sm={2}>
                    <Input type="currency" id="balanceTransferred" onChange={(e) => this.handleCurrency(e, 'transferred')} />
                </Col>
            </FormGroup>

            <FormGroup row>
                <Label for="balanceCashed" sm={4}>Cashed *</Label>
                <Col sm={2}>
                    <Input type="currency" id="balanceCashed" onChange={(e) => this.handleCurrency(e, 'cashed')} />
                </Col>
            </FormGroup>

            <FormGroup row>
                <Label for="balanceRate" sm={4}>Rate</Label>
                <Col sm={2}>
                    <Input type="currency" id="balanceRate" onChange={(e) => this.handleCurrency(e, 'rate')} />
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