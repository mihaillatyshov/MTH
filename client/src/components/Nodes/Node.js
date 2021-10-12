import React from 'react'

const Node = ( {node, onNodeChange} ) => {

	return (
		<div className="card">
			<div className="card-body">
				<div className="card-text">
					{node.desc}
				</div>
				<input className="btn btn-primary node-button" type="button" value="Go" onClick={(e) => onNodeChange(node.id)} /> 
			</div>
		</div>
	)
}

export default Node
