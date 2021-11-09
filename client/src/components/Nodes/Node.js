import React from 'react'
import { Link } from 'react-router-dom'
import cs from './Nodes.module.css'

const Node = ( {node} ) => {
	return (
		<Link to={"/graph/" + node.id} className={cs.node}>
			<div className={`card my-2 mx-2 node-pn`}>
				<div className="card-body">
					<h6 className="card-title">
						{node.name}
					</h6>
					<div className="card-text">
						{node.desc}
					</div>
				</div>
			</div>
		</Link>
	)
}

export default Node
