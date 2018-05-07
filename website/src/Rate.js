import React from 'react';
import { Button, Form, FormGroup, Label, Input, Col } from 'reactstrap';

export class Rate extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div class="form">
        <Form>
            <FormGroup row>
                <Label for="rateSource" sm={4}>Source</Label>
                <Col sm={2}>
                    <Input type="select" name="source" id="rateSource">
                        <option>EUR</option>
                        <option>GBP</option>
                        <option>NZD</option>
                    </Input>
                </Col>
            </FormGroup>
            <FormGroup row>
                <Label for="rateTarget" sm={4}>Target</Label>
                <Col sm={2}>
                    <Input type="select" name="target" id="rateTarget">
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
        <div id="output"></div>
      </div>
    )
  }
}