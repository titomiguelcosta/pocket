import React from 'react';
import { Button, Form, FormGroup, Label, Input, Col } from 'reactstrap';

export class Rate extends React.Component {
  constructor(props) {
    super(props);

        this.state = {
            description: null
        }
    }

  handleSubmit(e) {
    e.preventDefault()

    console.log(this.rate.value)

    fetch(`https://pocket.titomiguelcosta.com/rate/${this.source.value}/${this.rate.value}`)
        .then((res) => res.json())
        .then((data) => {
                console.log(data);

                this.setState({
                    description: data.description
                })
            })
  }

  render() {
    return (
      <div className="form">
        <Form onSubmit={(e) => this.handleSubmit(e)}>
            <FormGroup row>
                <Label for="rateSource" sm={4}>Source</Label>
                <Col sm={2}>
                    <Input type="select" name="source" id="rateSource" ref={(input) =>  {this.source = input}}>
                        <option>EUR</option>
                        <option>GBP</option>
                        <option>NZD</option>
                    </Input>
                </Col>
            </FormGroup>
            <FormGroup row>
                <Label for="rateTarget" sm={4}>Target</Label>
                <Col sm={2}>
                    <Input type="select" name="target" id="rateTarget" ref={(input) =>  {this.rate = input}}>
                        <option>EUR</option>
                        <option>GBP</option>
                        <option>NZD</option>
                    </Input>
                </Col>
            </FormGroup>

            <FormGroup>
                <Button>Calculate</Button>
            </FormGroup>
        </Form>
        <div id="output">{this.state.description}</div>
      </div>
    )
  }
}