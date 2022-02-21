import Head from 'next/head'
import { 
  Button,
  // ButtonGroup,
  // ButtonToolbar,
  Card,
  Col,
  Container,
  Nav,
  Row,
  // Stack
} from 'react-bootstrap'


import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faGithub } from '@fortawesome/free-brands-svg-icons'


import { LC } from '../components/charts';
import { QueryButtonToolbar } from '../components/queryButtonToolbar'

import dynamic from 'next/dynamic'
const CodeEditor = dynamic(import('../components/codeEditor'), {ssr: false})

export default function Home() {
  return (
    <Container className="md-container">
      <Head>
        <title>nearspark</title>
        <link rel="icon" href="/favicon-32x32.png" />
      </Head>
      <Container>
        <h1>
          Welcome to <a href="https://nextjs.org">nearspark</a>
        </h1>
        <p>
          Get started by querying the <code>blocks</code> table or the <code>gas</code> table.
        </p>
        <Container fluid className="mt-5">
          <Row>
            <Col md={3} className="border-left">
              <Nav className="flex-column">
                <Nav.Item>Blocks</Nav.Item>
                <Nav.Item>Gas</Nav.Item>
              </Nav>
            </Col>
            <Col md={9}>
              <CodeEditor />
            </Col>
          </Row>
          <Row className="mt-2">
            <Col md={3}></Col>
            <Col>
              <QueryButtonToolbar />
            </Col>
          </Row>
          <Row>
            <LC />
          </Row>
        </Container>
      </Container>

      <footer className="cntr-footer">
        <FontAwesomeIcon icon={faGithub} /> &nbsp;
        <a
          href="https://github.com/rnhttr/nearspark"
          target="_blank"
          rel="noopener noreferrer"
        >
          nearspark
        </a>
      </footer>
    </Container>
  )
}
