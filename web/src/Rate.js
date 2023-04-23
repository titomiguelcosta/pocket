import React from 'react';
import { Button, Form, FormGroup, Alert, Spinner } from 'reactstrap';
import { Currency } from './Currency';

export class Rate extends React.Component {
  constructor(props) {
    super(props);
    this.url = 'https://api.pocket.titomiguelcosta.com';
    this.state = {
      loading: false,
      description: null,
      source: 'EUR',
      target: 'NZD'
    };
  }

  handleSubmit(e) {
    e.preventDefault();
    this.setState({ description: null, loading: true });

    fetch(`${this.url}/rate/${this.state.source}/${this.state.target}`)
      .then((res) => res.json())
      .then((data) => {
        this.setState({ description: data.description, loading: false })
      })
      .catch((error) => {
        this.setState({ description: "Failed to connect.", loading: false })
      });
  }

  handleCurrency(e, widget) {
    this.setState({ [widget]: e.target.value });
  }

  render() {
    return (
      <div className="form">
        <Form onSubmit={(e) => this.handleSubmit(e)}>
          <Currency name="Source" field="source" default={this.state.source} handleCurrency={this.handleCurrency.bind(this)} />
          <Currency name="Target" field="target" default={this.state.target} handleCurrency={this.handleCurrency.bind(this)} />

          <FormGroup>
            <Button disabled={this.state.loading}>
              {
                this.state.loading &&
                <Spinner size="sm">{' '}</Spinner>
              }
              {
                !this.state.loading &&
                'Calculate'
              }
            </Button>
          </FormGroup>
        </Form>
        {
          !this.state.loading &&
          this.state.description &&
          <Alert color="dark" id="output">
            {this.state.description}
          </Alert>
        }
      </div>
    )
  }
}